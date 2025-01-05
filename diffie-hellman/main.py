
P = 23  # A prime number
G = 5   # A primitive root modulo P

private_A = 6  
public_A = (G ** private_A) % P  
private_B = 15  
public_B = (G ** private_B) % P  
shared_secret_A = (public_B ** private_A) % P 
shared_secret_B = (public_A ** private_B) % P  


assert shared_secret_A == shared_secret_B

print(f"Public Key A: {public_A}")
print(f"Public Key B: {public_B}")
print(f"Shared Secret: {shared_secret_A}")
