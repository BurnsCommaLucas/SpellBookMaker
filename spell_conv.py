import sys
import os

debug = False

def writer(line):
    if type(line) == list:
        for l in line:
            output(l)
    else:
        output(line)

def output(line):
    if debug:
        sys.stdout.write(line)
    else:
        o.write(line)

def header():
    writer("\\documentclass[10pt,twoside,twocolumn]{article}\n")
    writer("\\usepackage[bg-letter]{dnd} % Options: bg-a4, bg-letter, bg-full, bg-print, bg-none.\n")
    writer("\\usepackage[ngerman]{babel}\n")
    writer("\\usepackage[utf8]{inputenc}\n")
    writer("\\usepackage{enumitem}\n")
    writer("\\newlength{\\mylen}\n")
    writer("\\setbox1=\\hbox{$\\bullet$}\\setbox2=\\hbox{\\tiny$\\bullet$}\n")
    writer("\\setlength{\\mylen}{\\dimexpr0.5\\ht1-0.5\\ht2}\n\n")
    writer("% Start document\n")
    writer("\\begin{document}\n")
    writer("\\fontfamily{ppl}\\selectfont % Set text font\n\n")

def itemize():
    writer("\\renewcommand\\labelitemi{\\raisebox{\\mylen}{\\tiny$\\bullet$}}\n")
    writer("\\begin{itemize}\n")
    writer("\\setlength\\itemsep{-.25em}\n")

def enumerate():
    writer("\\begin{enumerate}[label=\\textbf{\\textit{\\arabic*.}}, wide, labelwidth=!, labelindent=8pt]\n")
    writer("\\setlength\\itemsep{-.25em}\n")

def endList():
    writer("\\end{" + ("itemize" if itemizing else "enumerate") + "}\n")

i = open(sys.argv[1])
outname = sys.argv[1][:-4] + ".tex" 
#outname = "writer.tex"
if not debug:
    o = open(outname, 'w')
header()
lines = i.readlines()
for i in range(0,len(lines)):
    line = lines[i].strip()
    if line.startswith("Level "):
        if not line.endswith("0"):
            writer("\\vfill\n")
        writer("\\section{" + line + "}\n")
    if line.startswith("Casting Time:"):
        ## SPELL DETAILS
        writer("\\subsection{" + lines[i-3].strip() + "}\n")
        writer("\\textit{" + lines[i-2].strip() + "}\n")
        writer("\\smallskip\n\n\\noindent\n")
        lineBuf = []
        for j in range(i, i+4):
            line = lines[j].strip()
            ind = line.index(":") + 1
            comp = line.startswith("Components")
            if comp:
                prev = len(lineBuf) - 1
                lineBuf[prev] = lineBuf[prev][:-3] + "\n\n\\noindent\n\\hangindent=1em\n"
            lineBuf.append("\\textbf{" + line[:ind] + "} " + line[ind:]
            + ("\n\n\\noindent\n" if comp else "\\\\\n"))
        writer(lineBuf)
        writer("\\smallskip\n\n")
        ## END SPELL DETAILS

        ## SPELL BODY
        itemizing = False
        enumerating = False
        while (not lines[j].startswith("Source:")):
            line = lines[j].strip()
            if line != "":
                fchar = line[0]
            else:
                fchar = ""

            if fchar == "-":
                if not itemizing:
                    itemizing = True
                    itemize()
                writer("\\item " + line[2:] + "\n")
            elif fchar.isdigit():
                if not enumerating:
                    enumerating = True
                    enumerate()
                writer("\\item \\textbf{\\textit{" + line[3:line.index(":")] + ".}} ")
            elif itemizing or enumerating and line != "":
                if lines[j-1][0].isdigit():
                    writer(line + "\n")
                else:
                    endList()
                    itemizing = False
                    enumerating = False
            elif not line.startswith("Duration:"):
                if line.startswith("At Higher Levels"):
                    ind = line.index(":")
                    writer("\\textbf{\\textit{" + line[:ind] + ".}}" + line[ind+1:])
                else:
                    writer(line + "\n")
                if not lines[j].startswith("\n") and lines[j].endswith("\n"):
                    writer("\n")
            j += 1 
        ## END SPELL BODY

        ## SPELL SOURCE
        if enumerating or itemizing:
            endList()
        line = lines[j].strip()
        ind = line.index(":") + 1
        writer("\\textit{" + line[:ind] + "}" + line[ind:] + "\n\n")
        ## END SPELL SOURCE
writer("\\end{document}") 
sys.exit(1 if debug else 0)