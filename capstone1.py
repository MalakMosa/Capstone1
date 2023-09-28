import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

class Data :
    def __init__(self,type_of_data,path_of_data):
        self.type_of_data=type_of_data
        self.path=path_of_data
    def read_data(self):
        if self.type_of_data=='csv':
           self.dataframe = pd.read_csv(self.path)
           print(self.dataframe)
        if  self.type_of_data=='excel' :
           self.dataframe = pd.read_excel(self.path)
           print(self.dataframe)
        if self.type_of_data=='sql' :
           self.dataframe = pd.read_sql(self.path)
           print(self.dataframe)
    def type_of_each_column(self):
        print(self.dataframe.dtypes)
    def handle_data(self):
        print('duplicated in data \n{}'.format(self.dataframe.duplicated()))
        self.handeled_data=self.dataframe.drop_duplicates('Year')
        print('drop duplicated in year\n{}'.format(self.handeled_data.drop_duplicates('Year')))
        print('your null data\n{}'.format(self.handeled_data.isna().sum()))
        print('remove nulls\n{}'.format(self.handeled_data.dropna()))
    def encode_Categorical_Data(self):
        encode_data=pd.DataFrame(self.handeled_data)
        encode_data=pd.get_dummies(encode_data,columns=['fg_apt'],drop_first=True)
        encode_data=pd.get_dummies(encode_data,columns=['usg_apt'],drop_first=True)
        encode_data=pd.get_dummies(encode_data,columns=['carrier'],drop_first=True)
        lx=LabelEncoder()
        encode_data['type']=lx.fit_transform(encode_data["type"])
        print(encode_data)

    def scaling_numerical_features(self):
        scaled_data = pd.DataFrame(self.handeled_data)
        scaler = MinMaxScaler(feature_range=(0, 100))
        scaled_data[['fg_wac']] = scaler.fit_transform(scaled_data[['fg_wac']])
        print('data after scaling:fg_wac\n{}'.format(scaled_data))
    def visualize_data(self):
        print("bar chart")
        count=self.handeled_data['fg_apt'].value_counts()
        count=pd.DataFrame(count)
        fig= plt.figure(figsize = (20, 5))
        fig2=plt.bar(count.T.columns,count['fg_apt'])
        plt.xlabel("fg_apt")
        plt.ylabel("count")
        plt.show()
        count=self.handeled_data['usg_apt'].value_counts()
        count=pd.DataFrame(count)
        fig= plt.figure(figsize = (20, 5))
        fig2=plt.bar(count.T.columns,count['usg_apt'])
        plt.xlabel("usg_apt")
        plt.ylabel("count")
        plt.show()
        count=self.handeled_data['carrier'].value_counts()
        count=pd.DataFrame(count)
        fig= plt.figure(figsize = (20, 5))
        fig2=plt.bar(count.T.columns,count['carrier'])
        plt.xlabel("carrier")
        plt.ylabel("count")
        plt.show()
        ###############################################
        print("histogram")
        plt.hist(self.handeled_data['Month'],edgecolor="red")
        plt.xlabel("Month")
        plt.ylabel("count")
        plt.show()
        values,bins,patches=plt.hist(self.handeled_data['airlineid'],bins=5,edgecolor="white",linewidth=3)
        plt.title('airlineid')
        plt.show()
        plt.hist(self.handeled_data['usg_wac'],edgecolor="white",)
        plt.title('usg_wac')
        plt.show()
        plt.hist(self.handeled_data['usg_apt_id'],edgecolor="white")
        plt.title('usg_apt_id')       
        plt.show()
        print("scatter")
        sns.pairplot(self.handeled_data)
        #############################################
        print("pie")
        counts=self.handeled_data["usg_apt"].value_counts()
        plt.figure(figsize=(7,7))
        plt.pie(counts,labels=counts.index.values.tolist())
        plt.show()
my_data=Data('csv','International_Report_Departures.csv')
my_data.read_data()
my_data.type_of_each_column()
my_data.handle_data()
my_data.encode_Categorical_Data()
my_data.scaling_numerical_features()
my_data.visualize_data()
