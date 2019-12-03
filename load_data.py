import os
import json
import pandas as pd

class DataLoader:
    def __init__(self, path, columns=['published', 'title', 'text']):
        self.path = path
        self.columns = columns

    def read_json(self):
        json_files = (os.path.join(path, file)
                      for path, subdirs, files in os.walk(self.path)
                      for file in files
                      if file.endswith('.json'))
        df = pd.DataFrame(columns=self.columns)

        for index, file in enumerate(json_files):
            with open(file, encoding='utf-8') as json_data:
                raw_data = json.load(json_data)
                data = {key: raw_data[key] for key in self.columns}
                temp = pd.DataFrame(data, index=[index])
                df = df.append(temp)

        df.published = pd.to_datetime(df.published)
        return df.sort_values('published').reset_index(drop=True)


if __name__ == '__main__':
    a = DataLoader("C://Users//olesia.tretiak//PycharmProjects//finnews//webhose datasets-20191202T121109Z-001//webhose datasets")
    df = a.read_json()
