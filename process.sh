#!/bin/bash

# process.sh <thumb directory> <output file>

echo "" > $2

for f in $1/thumb*png; do
  echo "# $f #" >> $2
  
  echo "## round ##" >> $2
  # crop the round timer region
  convert $f -crop 55x18+312+70 png:- | tesseract stdin stdout ./round.config >> $2

  echo "## name ##" >> $2
  # crop the name region, send it through ocr
  convert $f -crop 225x35+110+970 png:- | tesseract stdin stdout >> $2

  rm $f
done
