# w2vec_gen 
This project provides dynamically generating word2vec from csv file.  
For installation :  
Simply
```
  make install
``` 
Usage:  

```
python3 src/w2vec.py -c </Users/.../data.csv> -t <target_column_name>
```

Which is the data source, the name of the column to be used for w2vec training and the path of the csv file are added to the script as arguments as above. The value of the sep as  default ",". 
If sep value is wanted to be changed, -s parameter is added to the command as follows. As a result of the all process, the w2vec model is saved under the "model" folder with the name "w2v.bin". Do not forget to empty the "model" folder before starting the training.
```
python3 src/w2vec.py -c /Users/.../data.csv -t <target_column_name> -s <new_sep_value>
```
 
-------------------------
## Docker

If you want to use this project via docker (default image name --> w2vec-gen): 
```
  make docker
``` 
Usage: 
```
make docker_run csv_path=</Users/.../data.csv> target_column=<target_column_name>
```


Volume operations are performed automatically. The model created as a result of the operations performed via Docker are added to the "model" folder on the server/local machine.

-------------------------
## TODO

* Test
