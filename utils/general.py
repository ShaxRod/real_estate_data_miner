import pandas as pd

class data_structure_format:

    def nest_dict_to_dataframe(self, nest_dict : dict):

        df = pd.DataFrame(nest_dict)
        df = df.swapaxes('index', 'columns')
        return df