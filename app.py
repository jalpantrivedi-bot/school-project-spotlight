# ==========================================================
#        SLEEP KINGDOM: EXTREME CHAOS EDITION 😈💤
#        Harder + Cleaner + Funnier Python Game
# ==========================================================

import random
import time
import streamlit as st

# ---------------- PLAYER ----------------

class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.happiness = 100
        self.money = 50
        self.braincells = 100
        self.day = 1

    def show_stats(self):
        st.write("\n" + "=" * 45)
        st.write(f"😎 PLAYER: {self.name}")
        st.write("=" * 45)
        st.write(f"⚡ Energy     : {self.energy}")
        st.write(f"😂 Happiness  : {self.happiness}")
        st.write(f"💰 Money      : ${self.money}")
        st.write(f"🧠 Braincells : {self.braincells}")
        st.write(f"📅 Day        : {self.day}")
        st.write("=" * 45)

# ---------------- FUNCTIONS ----------------

def pause():
    time.sleep(1)

def clamp_stats(player):
    player.energy = max(0, min(100, player.energy))
    player.happiness = max(0, min(100, player.happiness))
    player.braincells = max(0, min(100, player.braincells))

def random_event(player):

    events = [

        ("💀 You stepped on LEGO barefoot.", -20, -5, 0),

        ("🐔 A chicken stole your wallet.", 0, -10, -20),

        ("📱 You watched brain rot videos for 5 hours.", -15, +10, -20),

        ("🍕 Free pizza appeared from the sky.", +15, +15, 0),

        ("🦆 Angry duck attack!", -25, -10, 0),

        ("👽 Aliens upgraded your socks.", +5, +20, +10),

        ("🚽 Toilet explosion. Don't ask.", -15, -15, -5),

        ("🛌 You accidentally slept through school/work.", +20, -10, 0)

    ]

    event = random.choice(events)

    st.write("\n🌎 RANDOM EVENT")
    st.write("-" * 45)
    pause()

    st.write(event[0])

    player.energy += event[1]
    player.happiness += event[2]
    player.money += event[3]

# ---------------- GAME START ----------------

st.write("=" * 55)
st.write("🌙 WELCOME TO SLEEP KINGDOM 🌙")
st.write("💀 HARD MODE ACTIVATED")
st.write("=" * 55)

name = st.text_input("\nEnter your name: ")

player = Player(name)

# ---------------- MAIN GAME LOOP ----------------

while True:

    clamp_stats(player)

    # --------- Lose Conditions ---------

    if player.energy <= 0:
        st.write("\n💀 You died from exhaustion.")
        break

    if player.braincells <= 0:
        st.write("\n🧠 You lost all braincells.")
        st.write("🥔 You are now a potato.")
        break

    if player.happiness <= 0:
        st.write("\n😭 Depression defeated you.")
        break

    if player.money <= -50:
        st.write("\n💸 You became too broke to survive.")
        break

    # --------- Win Condition ---------

    if player.day > 15:
        st.write("\n🏆 YOU SURVIVED 15 DAYS!")
        st.write("👑 You are officially the Sleep King.")
        break

    # --------- Display Stats ---------

    player.show_stats()

    # --------- Menu ---------

    st.write("\nChoose your action:")
    st.write("1. 😴 Sleep")
    st.write("2. 🎮 Game All Night")
    st.write("3. 🍔 Eat Mystery Food")
    st.write("4. 💼 Work Weird Job")
    st.write("5. 👹 Fight Sleep Demon")
    st.write("6. 📱 Watch Brain Rot")
    st.write("7. 🚽 Think About Life")
    st.write("8. 🎰 Gamble Money")
    st.write("9. 🚪 Quit")

    choice = st.text_input("\nEnter choice: ")

    # ======================================================
    # SLEEP
    # ======================================================

    if choice == "1":

        st.write("\n😴 You go to sleep...")
        pause()

        dreams = [
            "🐸 Frog lawyers chased you.",
            "🍞 Bread called you ugly.",
            "🚀 You became king of the moon.",
            "🦖 Dinosaur stole your homework."
        ]

        st.write(random.choice(dreams))

        gain = random.randint(15, 35)

        player.energy += gain
        player.happiness += 5

        st.write(f"✨ Energy +{gain}")

    # ======================================================
    # GAMING
    # ======================================================

    elif choice == "2":

        st.write("\n🎮 GAMING ALL NIGHT")
        pause()

        outcomes = [
            "💀 A 9-year-old destroyed you online.",
            "🔥 You screamed at lag for 2 hours.",
            "🐔 Internet disconnected during victory.",
            "🗿 You played farming simulator competitively."
        ]

        st.write(random.choice(outcomes))

        energy_loss = random.randint(20, 35)

        player.energy -= energy_loss
        player.happiness += 15
        player.braincells -= 10

        st.write(f"⚡ Energy -{energy_loss}")

    # ======================================================
    # FOOD
    # ======================================================

    elif choice == "3":

        foods = [

            ("☢️ Gas Station Sushi", +10, -25),

            ("🍕 3AM Pizza", +20, +5),

            ("🗿 Mystery Meat", +5, -40),

            ("🌮 Taco Of Destiny", +25, -10),

            ("🧃 Suspicious Juice", -15, -20)

        ]

        food = random.choice(foods)

        st.write(f"\n🍴 You ate {food[0]}")
        pause()

        player.energy += food[1]
        player.braincells += food[2]
        player.money -= 15

        st.write("🤢 Terrible decision.")

    # ======================================================
    # JOB
    # ======================================================

    elif choice == "4":

        jobs = [
            "🐟 Fish Translator",
            "🦆 Duck Therapist",
            "🍟 French Fry Engineer",
            "🧹 Professional Dust Inspector"
        ]

        job = random.choice(jobs)

        st.write(f"\n💼 Working as: {job}")
        pause()

        earned = random.randint(20, 60)
        loss = random.randint(15, 30)

        player.money += earned
        player.energy -= loss

        st.write(f"💰 Money +${earned}")
        st.write(f"⚡ Energy -{loss}")

    # ======================================================
    # DEMON FIGHT
    # ======================================================

    elif choice == "5":

        demon = random.randint(25, 70)

        st.write("\n👹 SLEEP DEMON APPEARS")
        st.write(f"💀 Demon Power: {demon}")

        pause()

        attack = random.randint(10, 60)

        st.write(f"⚔️ Your attack power: {attack}")

        if attack >= demon:

            reward = random.randint(30, 80)

            st.write("\n🏆 DEMON DEFEATED")
            st.write("💰 You stole the demon's lunch money.")

            player.money += reward
            player.happiness += 20

        else:

            damage = demon - attack

            st.write("\n💥 The demon hit you with a chair.")

            player.energy -= damage
            player.braincells -= 15

            st.write(f"⚡ Energy -{damage}")

    # ======================================================
    # BRAIN ROT
    # ======================================================

    elif choice == "6":

        st.write("\n📱 Watching brain rot...")
        pause()

        videos = [
            "🐵 Monkey dancing for 9 hours.",
            "🗿 Sigma cucumber motivation edit.",
            "🍞 Bread falling in slow motion.",
            "🐈 Cat becomes CEO."
        ]

        st.write(random.choice(videos))

        player.happiness += 20
        player.braincells -= random.randint(20, 35)
        player.energy -= 10

    # ======================================================
    # TOILET
    # ======================================================

    elif choice == "7":

        st.write("\n🚽 You sit and think deeply...")
        pause()

        thoughts = [
            "🤔 Why is pizza round but boxes square?",
            "🤔 Are fish thirsty?",
            "🤔 Maybe bananas are soft boomerangs.",
            "🤔 What if dogs think humans are weird?"
        ]

        st.write(random.choice(thoughts))

        player.happiness += 10
        player.energy += 5

    # ======================================================
    # GAMBLE
    # ======================================================

    elif choice == "8":

        st.write("\n🎰 GAMBLING TIME")
        pause()

        if player.money < 10:
            st.write("💸 Too broke to gamble.")
        else:

            bet = random.randint(10, 30)

            st.write(f"💰 You bet ${bet}")

            if random.randint(1, 100) <= 35:

                winnings = bet * 2

                st.write("🏆 YOU WON!")
                player.money += winnings

            else:

                st.write("💀 YOU LOST EVERYTHING.")
                player.money -= bet

    # ======================================================
    # QUIT
    # ======================================================

    elif choice == "9":

        st.write("\n👋 You escaped the chaos.")
        break

    # ======================================================
    # INVALID
    # ======================================================

    else:
        st.write("\n❌ Invalid choice.")
        continue

    # --------- Daily Drain ---------

    player.energy -= random.randint(5, 15)
    player.happiness -= random.randint(3, 10)

    # --------- Random Event ---------

    random_event(player)

    # --------- Next Day ---------

    player.day += 1

# ---------------- END SCREEN ----------------

st.write("\n" + "=" * 55)
st.write("🎮 THANKS FOR PLAYING SLEEP KINGDOM")
st.write("=" * 55)
