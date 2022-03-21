import re
from pathlib import Path
from shutil import copy

IMAGES_PATTERN = r"images = \[\"(.*)\"\]"


def main() -> None:
    website_languages = Path(Path(__file__).parent.parent / "content").glob("*/")
    for website_language in website_languages:
        content_directory = website_language / "posts/"
        if not content_directory.exists():
            continue
        for directory in content_directory.iterdir():
            if not directory.is_dir():
                continue
            if not directory.glob("images/*"):
                continue
            print(directory)
            content_file = directory / "index.md"
            if not content_file:
                print(f"No content file found in {directory}")
                continue
            post_content = content_file.read_text(encoding="utf-8")
            post_current_thumbnail = re.search(IMAGES_PATTERN, post_content)
            if not post_current_thumbnail:
                print(f"No thumbnail found in {content_file}")
                continue
            post_current_thumbnail = post_current_thumbnail.group(1)
            new_thumbnail_path = (
                directory / f"thumbnail-{post_current_thumbnail.split('/')[-1]}"
            )
            (directory / post_current_thumbnail).rename(new_thumbnail_path)
            post_new_content = re.sub(IMAGES_PATTERN + "\n", "", post_content)
            post_new_content = post_new_content.replace(
                post_current_thumbnail,
                f"thumbnail-{post_current_thumbnail.split('/')[-1]}",
            )
            content_file.write_text(post_new_content, encoding="utf-8")
            print(f"Migrated {content_file}")


if __name__ == "__main__":
    main()
