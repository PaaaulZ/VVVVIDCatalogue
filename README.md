# VVVVIDCatalogue
A catalogue for popular italian anime site VVVVID that supports searching and a full list instead of having to choose a letter of the alphabet

## DISCLAIMER:

This is just a catalogue! 
All it does is show every anime available on VVVVID in a single page instead of having to choose letter by letter and supports searching.
This does not download, store or copy any video or data. When launched it will load the anime list, show the catalogue with links pointing to VVVVID and when you close it everything is gone.

## Why?

1) VVVVID does not support searching.
2) VVVVID does not give you an overview of available titles, you have to trust the "Popular" section or choose a letter of the alphabet.
3) Even if you know a letter or trust the "Popular" section you have to scroll horizontally to view every title while the background keeps moving and the whole screen is full of text and buttons that you don't need / don't want.

## How to run?

1) Clone this repository and navigate to the folder.
2) Install requirements:
```
pip3 install -r requirements.txt
```

3) Run:

Linux:
```bash
$ export FLASK_APP=catalogue
$ flask run
```

Windows:
```batch
> set FLASK_APP=catalogue
> flask run
```

4) Navigate to: http://127.0.0.1:5000/ and enjoy (wait a minute or two for the list to load)

## Live version:

Click [HERE](https://paaaulz.github.io/VVVVIDCatalogue) for a live version. 
This version is not always updated and has no search bar, you can still search by using your browser's search function (CTRL + F).