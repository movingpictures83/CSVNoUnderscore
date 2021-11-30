class CSVNoUnderscorePlugin:
    def input(self, myfile):
       self.infile = open(myfile, 'r')

    def run(self):
        pass

    def output(self, myfile):
      outfile = open(myfile, 'w')

      firstline = self.infile.readline()
      outfile.write(firstline)

      for line in self.infile:
          firstitem = line[:line.find(',')]
          newfirst = firstitem.replace('_', '')
          line = line.replace(firstitem, newfirst)
          outfile.write(line)
