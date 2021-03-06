"""Functions and utilities related to importing and exporting files."""

import pathlib
import typing

from image_utils import SUPPORTED_IMAGE_EXTENSIONS


def list_file_paths(directory: pathlib.Path) -> typing.List[pathlib.Path]:
    """Returns a list of full paths to all the files that are direct children.

    Does not include directories or files in subdirectories.

    Params:
      directory: The full path to the directory to look for files in.

    Returns:
      List of paths to the files found.
    """
    return [item for item in directory.iterdir() if item.is_file()]


def filter_by_extensions(files: typing.Sequence[pathlib.Path],
                         extensions: typing.List[str]
                         ) -> typing.List[pathlib.Path]:
    """Filter a list of Paths by a list of extensions.

    Params:
      files: A list of Path objects.
      extensions: List of file extensions, with leading dots (ie, `[".txt",
        ".tar.gz"]`).

    Returns:
      A filtered list of the same path objects, *not* copies of the original
        objects.
    """
    return [file for file in files if "".join(file.suffixes) in extensions]


def filter_images(files: typing.Sequence[pathlib.Path]
                  ) -> typing.List[pathlib.Path]:
    """Filter a list of Paths and return only the images."""
    return filter_by_extensions(files, SUPPORTED_IMAGE_EXTENSIONS)
