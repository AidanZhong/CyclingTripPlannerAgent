# -*- coding: utf-8 -*-
"""
Created on 19/01/2026 21:38

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: chat_cli

This is a CLI for the chatbot
"""
import requests

API_URL = "http://localhost:8080/chat"

if __name__ == '__main__':
    print("Cycling Trip Planner Agent CLI")
    print("Type 'quit' to exit")
    session_id = None
    while True:
        user_input = input("> ")
        if user_input == "quit":
            break
        if user_input == 'new':
            session_id = None

        payload = {"message": user_input}
        if session_id:
            payload["session_id"] = session_id

        r = requests.post(API_URL, json=payload)
        if r.status_code != 200:
            print(f"Error: {r.text}")

        data = r.json()
        session_id = data["session_id"]
        print(f"\nAgent> {data['reply']}\n")
