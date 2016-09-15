# batchRename
# Program that renames all files after its parent folder with an index

C://.../A-folder/B-folder/fila_A.txt
C://.../A-folder/B-folder/fila_B.txt
C://.../A-folder/C-folder/fila_1.txt
C://.../A-folder/C-folder/fila_2.txt

Copy this program to A_folder and start it, it will go through all folders in A-folder and rename all files inside these folders after its parent folder

Therefore 
C://.../A-folder/B-folder/fila_A.txt ---->>>> C://.../A-folder/B-folder/B-folder 1.txt
C://.../A-folder/B-folder/fila_B.txt ---->>>> C://.../A-folder/B-folder/B-folder 2.txt
C://.../A-folder/C-folder/fila_1.txt ---->>>> C://.../A-folder/C-folder/C-folder 1.txt
C://.../A-folder/C-folder/fila_2.txt ---->>>> C://.../A-folder/C-folder/C-folder 2.txt

Didnt invest much time into that, so beware of these limitations
1. Make sure that in A-folder there are _only_ folders with files inside and there are no folders inside B-folder. 
2. Program will make a copy of itself. You'll have to remove it manually.
3. Please make sure you test it on test files. 


Obviously feel free to modify it to suit your needs and remove bugs. 
