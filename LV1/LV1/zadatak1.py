print("Input hours:")
sati=int(input())
print("Input wage per hour")
satnica=float(input())

def total_euro():
    return sati*satnica

print(f"Paycheck :{total_euro()} €" )