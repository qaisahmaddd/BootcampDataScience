import pandas as pd

class DataLoader:
    def __init__(self, format, path, sheet=None):
        self.format = format
        self.path = path
        self.sheet = sheet

    def load_data(self):
        if self.format == 'csv':
            return pd.read_csv(self.path)
        elif self.format == 'excel':
            if self.sheet is None:
                return pd.read_excel(self.path)
            else:
                return pd.read_excel(self.path, sheet_name=self.sheet, header=0)
    
    def color(self):
        color_codes= {
            1: '#193154',
            2: '#e3b505',
            3: '#95190c',
            4: '#107e7d',
            5: '#cfccd6'
        }
        return color_codes
