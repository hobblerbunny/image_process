import os
import pandas as pandas
from torch.utils.data import Dataset
from skimage import io

class sourcecontent(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.file = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.file)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.file.iloc(index, 0))
        image = io.read(img_path)
        y_label = torch.tensor(int(self.file.iloc[index, 1]))
        
        if self.transform(image):
            image = self.transform(image)

        return self.transform(image)


