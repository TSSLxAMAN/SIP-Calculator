from matplotlib import pyplot as plt
import os

def sip_calcoualtor(amount, rate,time):
    interest = (rate / 100)/12
    x = amount * (((1 + interest)**(time* 12) - 1) / interest) * (interest+1)
    return x

# HANDLING CACULATION
print("\n========== Welcome to SIP calculator ==========\n")
sip_name = input("      Enter the name of SIP : ")
amount = int(input("      Money investment deposit per month : "))
rate = int(input("      Expected return rate per year (in %) : "))
time  = int(input("      Time period in years : "))
future_value = sip_calcoualtor(amount, rate, time)
future_value = round(future_value,2)
estimated_returns = future_value - (amount * 12)*time
total_invested_amount = (amount * 12)*time
print(f"""
    ========== {sip_name} ==========
    Money Invested per month : {amount}
    Interest : {rate}%
    Time : {time} years

    Total invested amount : {total_invested_amount}
    Estimated returns : {estimated_returns}
    Total Amount : {future_value}
    """)

# HANDLING FILE
try:
    file_path = rf"C:\Users\Friends\Desktop\Projects\SIP_LOGS\{sip_name}.txt"
    with open(file_path,'w') as file:
        file.write(f"""
        SIP Name : {sip_name}
        Money Invested per month : {amount}
        Interest : {rate}%
        Time : {time} years
        Total invested amount : {total_invested_amount}
        Estimated returns : {estimated_returns}
        Total Amount : {future_value}
            """)
except Exception as e:
    print(e)
file = open(f"{sip_name}.txt","w")
file.write(f"""
        SIP Name : {sip_name}
        Money Invested per month : {amount}
        Interest : {rate}%
        Time : {time} years
        Total invested amount : {total_invested_amount}
        Estimated returns : {estimated_returns}
        Total Amount : {future_value}
            """)
# HANDLING PIE CHART
lable = ["Invested Value","Gained Value"]
size = [total_invested_amount,estimated_returns]
explode = (0.1,0.0)
plt.pie(size, labels= lable, explode=explode,shadow=True,)
plt.title(f"{sip_name}")
plt.legend(lable,loc = 4)
plt.text(-2.0,-1.5,f"Invested Value : {total_invested_amount}\nGained Value : {estimated_returns}\nTotal returns : {future_value}",fontsize = 12, bbox = dict(facecolor = "yellow",alpha = 0.5))
save_path = rf'C:\Users\Friends\Desktop\Projects\SIP_LOGS\{sip_name}.pdf'
try:
    plt.savefig(save_path)
except Exception as e:
    print(e)
plt.savefig(f"{sip_name}.pdf")
plt.show()