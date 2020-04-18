from convert import convert
import os

dir = os.getcwd()
os.chdir(dir + "\\dane_wejsc")

convert("topojson", "topojson")