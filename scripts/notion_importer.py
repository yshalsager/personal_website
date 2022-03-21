"""
A script to import notes from Notion as markdown.
"""
import re
from datetime import datetime
from os import environ
from pathlib import Path
from string import Template
from typing import Dict, List

import httpx
from notion import Notion2Markdown
from notion_client import Client

content_path = Path(__file__).parent.parent / "content/ar/notes/"

hugo_file_head = Template(
    """+++
title = "$post_title"
date = "$date"
layout = "docs"
type = "docs"
tags = ["ملاحظات"]
+++
**معلومات الكتاب**:

|               |                    |
| :------------: |   :-----------:   |
|  **عنوان الكتاب**  |    $title     |
|     **المؤلف**     |    $author    |
|     **الناشر**     |  $publisher   |
|   **سنة النشر**    | $publish_date |
|  **عدد الصفحات**   |    $pages     |
| **تاريخ القراءة**  |  $read_date   |
"""
)

notion = Client(auth=environ["NOTION_TOKEN"])
book_notes_request: Dict = {
    "database_id": "5677c26a86304eb5b65eb8f4a02a0657",
    # "page_size": 20,
    "filter": {
        "property": "processed",
        "checkbox": {
            "equals": True,
        },
    },
    "sort": {
        "property": "last_edited_time",
        "timestamp": "last_edited_time",
        "direction": "descending",
    },
}


def get_database(request: Dict) -> List[Dict]:
    pages = notion.databases.query(**request)
    results: List[Dict] = pages["results"]
    while pages["has_more"]:
        request["start_cursor"] = pages["next_cursor"]
        pages = notion.databases.query(**request)
        results.extend(pages["results"])
    return results


def main():
    last_run = datetime.strptime(
        Path("last_run").read_text(encoding="utf-8").strip(), "%Y-%m-%d %H:%M:%S"
    )
    book_pages: List[Dict] = get_database(book_notes_request)
    for book_page in book_pages:
        page_last_modified = datetime.strptime(
            book_page["last_edited_time"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        if page_last_modified <= last_run:
            continue
        book_title = book_page["properties"]["اسم الكتاب"]["title"][0]["plain_text"]
        print(book_title)
        try:
            book_markdown = Notion2Markdown(
                environ["NOTION_TOKEN"], book_page["id"]
            ).parse()
        except AttributeError as err:
            print(f"WARNING: Unable to parse page {book_title}. Exception: {err}")
            continue
        # replace KOReader Page number lines with dash
        book_markdown = re.sub(r"Page.*:\n", "- ", book_markdown)
        sub_title = book_page["properties"]["العنوان الفرعي"]["rich_text"]
        if sub_title:
            book_title += f" {sub_title[0]['plain_text']}"
        author = book_page["properties"]["المؤلف"]["rich_text"][0]["plain_text"]
        title = f"{book_title} - {author}"
        publisher = book_page["properties"]["الناشر"]["rich_text"][0]["plain_text"]
        publish_date = str(book_page["properties"]["سنة النشر"]["number"])
        pages_count = str(book_page["properties"]["الصفحات"]["number"])
        read_date = book_page["properties"]["تاريخ القراءة"]["date"]["start"]
        # cover = book_page["properties"]['الغلاف']['files'][0]['name']
        cover = book_page["icon"].get("external", {}).get("url", None) or book_page[
            "icon"
        ].get("file", {}).get("url", None)
        cover_image_name = f"thumbnail-image.{cover.split('.')[-1].split('?')[0]}"
        post_text = (
            hugo_file_head.substitute(
                post_title=title,
                date=read_date,
                title=book_title,
                author=author,
                publisher=publisher,
                publish_date=publish_date,
                pages=pages_count,
                read_date=read_date,
            )
            + "\n\n"
            + book_markdown
        )
        post_path = Path(content_path / f"books/{title}")
        post_path.mkdir(parents=True, exist_ok=True)
        Path(f"{post_path}/index.md").write_text(post_text, encoding="utf-8")
        Path(f"{post_path}/{cover_image_name}").write_bytes(httpx.get(cover).content)
    Path("last_run").write_text(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
