#BSUB -J passvar[1-5]
#BSUB -e logs/passvar.%I.%J.err
#BSUB -o logs/passvar.%I.%J.out
#BSUB -R "span[hosts=1]"
#BSUB -n 10

#INDIR=/vol3/home/liggettl/ExperimentalScripts/inputFiles
#OUTDIR=/vol3/home/liggettl/ExperimentalScripts/outputFiles

#files=(one
#two
#three
#four
#five)

#currentfile=${files[$(($LSB_JOBINDEX - 1))]}

#Can then run the file like this:
#python passVars.sh "${currentfile}"

one=1
two=2
three=3
four=4
five=5

python takeVars.py "$one" "$two" "$three" "$four" "$five"
