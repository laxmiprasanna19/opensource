
inputs = input().split()
vignesh = inputs[0]
charan = inputs[1]


if (vignesh == 'R' and charan == 'S') or (vignesh == 'P' and charan == 'R') or (vignesh == 'S' and charan == 'P'):
    print("Vignesh")
elif (charan == 'R' and vignesh == 'S') or (charan == 'P' and vignesh == 'R') or (charan == 'S' and vignesh == 'P'):
    print("Charan")
else:
    print("NULL")
