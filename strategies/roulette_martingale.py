import random

def martingale_simulation(starting_balance, initial_bet, rounds):
    balance = starting_balance
    bet = initial_bet
    history = []

    print(f"--- Starting Simulation: {rounds} rounds ---")
    
    for i in range(1, rounds + 1):
        if balance <= 0:
            print("❌ Bankrupt!")
            break
            
        # Simulate European Roulette (1-36, plus 0)
        # Betting on Red (18/37 chance)
        win = random.randint(0, 36) <= 18 
        
        if win:
            balance += bet
            history.append(f"Round {i}: WIN  | New Balance: ${balance}")
            bet = initial_bet  # Reset bet after win
        else:
            balance -= bet
            history.append(f"Round {i}: LOSS | New Balance: ${balance}")
            bet *= 2  # Double the bet after loss
            
        if bet > balance:
            bet = balance # Can't bet more than you have

    return balance, history

# Parameters
final_balance, log = martingale_simulation(starting_balance=1000, initial_bet=10, rounds=20)

for line in log[-10:]: # Show last 10 rounds
    print(line)
