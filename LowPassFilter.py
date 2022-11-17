class Filter:
    ts = 0.1;
    tf = 15*ts;
    filterValue = 0;
    init = True;
    def FilterValue(self,inn):
        if self.init :
            self.init = False
            self.filterValue = inn
        a = self.ts/(self.tf+self.ts)
        self.filterValue = (1-a)*self.filterValue+a*inn;
        return round(self.filterValue,2);
