# SpellBookMaker

Effectively a fork from [evanbergeron's DND 5e LaTeX Template](https://github.com/evanbergeron/DND-5e-LaTeX-Template) with a couple scripts tossed in. 

Takes as input a `.txt` file in the default format from SpellViewer, parses it into an okay `.tex` file, and turns that into a `.pdf`. 

## How to run it
Clone the repository and put your desired spellbook's `.txt` file in the directory. Run:

```
./maker.sh <spellbook_filename>
```

and then wait for the PDF to pop up.


## System Requirements
`python`, `pdflatex`, and some form of unix shell should be installed on your system before trying to run this.  

Some basic understanding of `LaTeX` wouldn't be bad either, though you can get away with googling things very easily once the initial `.tex` file is built.

---

## BAD THINGS

This is just to take *most* of the work out of converting these files, so there are a lot of tweaks left to do (please open an issue if you see something I haven't listed below). I do plan to fix the ones in my power, but for now here are the big ones: 

- I'd reccommend saving your `.tex` file somewhere else if you plan to edit it, just so you don't overwrite it with these scripts
- I don't know how this will interact with spell tables (Creation, Control Weather, Scrying, etc) so be prepared for them to not look like much
- Spells with bolded paragraph headers (Enhance Ability, Glyph of Warding, Imprisonment, etc.) will not have those headers bolded automatically
- Some spell text in SpellViewer is slightly different, so if things are supposed to be in a list form, you'll want to double check the formatting
- Okay probably just double check the formatting anyway, the input text varies wildly (extra spaces, 1d10 actually says 1dIO), and you'll want to add some `\vfill`s and such to make things line up with pages nicely
- Sometimes the pdf will build with the background image shoved up into one corner, which you can usually fix by building it again