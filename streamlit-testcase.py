from time import sleep
import streamlit as st

bell = 'ON'

form = st.sidebar.form(key="myform")
stop_loss_target_total = form.number_input("SL Target", value=int(600))
profit_target_total = form.number_input("Profit Target", value=int(800))
sleep_interval = form.number_input("Sleep Interval", value=int(3))
start = form.form_submit_button("Start")
stop = st.sidebar.button("Stop")

def print_parameter_values():
    print(f'\tSleep Interval: {sleep_interval} Secs')
    print(f'\tProfit Target (per lot): {profit_target_total}')
    print(f'\tStop Loss (per lot): {stop_loss_target_total}')
    print(f'\tBell: {bell}')
    # print(f'\n')

print('Waiting for connection…')
print("Connected…")
if bell == 'ON':
    print(f'Bell: {bell}')

print(start, stop)

def run_strategy():
    i = 0
    while True:
        print(i, start, stop)
        print(f'Current Parameters For The Run:')
        print_parameter_values()
        print(f'Hi2 {start}, {stop}')
        sleep(sleep_interval)
        i = i+1

if start:
    print('In start')
    print(start)
run_strategy()
if stop:
    print('In stop')
    print(stop)
    st.write('Exiting…')




