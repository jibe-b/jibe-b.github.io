#!/bin/env/python

def test_caracter(car_in, car_out col, line):
  if car=='\"':
    pass
  if car == ',':
    car_out = '|'
  if car == ' ':
    car_out = ' '
  if car == EOL:
    car_out = EOL
    line += 1


def write_file(car_out):
  g.write(car_out)

main():
  """This script converts csv files into tables using the Markdown syntax.
The question of the platefrom-dependent EOL (End Of Line) caracter has not been considered yet.
In this version, the output file must exist before running the script."""

  prompt input_file, output_file

  global EOL = '\n'    #Global variable used to enable plateform-dependent execution

#Calculating the length of the input file
  f = open(file, 'r')
  all = read()
  length = len(all)
  f.close()



#Initializing for reading
  f = open(input_file, 'r')
  car_out = ''
  col = 0
  line = 0

#Initializing for writing
  global g = open(output_file, 'a')
  
  

  while col < length :
    car = f.read(1)
    test_caracter(car, car_out, col, line)
    write_file(output, car_out)
    if line = 1 && col == 0:
      car_out = '|'
      while i < col :
        car_out += '---|'
      car_out += EOL
      write_file(car_out)
    col += 1

  f.close()
  g.close()
