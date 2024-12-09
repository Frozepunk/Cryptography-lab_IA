def rail_fence_func(text,key):
    rail=['']*key
    idx,step=0,1
    for char in text:
        rail[idx] += char
        idx += step
        if idx==0 or idx == key-1:
            step *= -1
    return ''.join(rail)
# USER INPUT
text=input("Enter the text")
key=int(input("Enter the key value"))
print(rail_fence_func(text,key))