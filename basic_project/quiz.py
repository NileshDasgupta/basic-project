questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B",
        "solution": "Paris is the capital and largest city of France."
    },

    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "C",
        "solution": "Mars appears reddish because of iron oxide (rust) on its surface."
    },

    {
        "question": "How many sides does a hexagon have?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B",
        "solution": "A hexagon is a polygon with six sides."
    },

    {
        "question": "Which language is primarily used to create web pages?",
        "options": ["A. Python", "B. C++", "C. HTML", "D. Java"],
        "answer": "C",
        "solution": "HTML (HyperText Markup Language) is used to structure web pages."
    },

    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D",
        "solution": "The Pacific Ocean is the largest and deepest ocean on Earth."
    },

    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Leo Tolstoy"],
        "answer": "A",
        "solution": "William Shakespeare wrote Romeo and Juliet."
    },

    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Au", "C. Gd", "D. Go"],
        "answer": "B",
        "solution": "The chemical symbol for gold is Au, from the Latin word 'aurum'."
    },

    {
        "question": "Which device is used to measure temperature?",
        "options": ["A. Barometer", "B. Ammeter", "C. Thermometer", "D. Voltmeter"],
        "answer": "C",
        "solution": "A thermometer is used to measure temperature."
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Computer Processing Utility"
        ],
        "answer": "A",
        "solution": "CPU stands for Central Processing Unit, the main processor of a computer."
    },

    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["A. China", "B. South Korea", "C. Japan", "D. Thailand"],
        "answer": "C",
        "solution": "Japan is traditionally known as the Land of the Rising Sun."
    },

    {
        "question": "What is the approximate speed of light in vacuum?",
        "options": [
            "A. 3 × 10^6 m/s",
            "B. 3 × 10^8 m/s",
            "C. 3 × 10^10 m/s",
            "D. 3 × 10^12 m/s"
        ],
        "answer": "B",
        "solution": "Light travels through vacuum at approximately 3 × 10^8 metres per second."
    },

    {
        "question": "Which data structure follows the LIFO principle?",
        "options": ["A. Queue", "B. Array", "C. Stack", "D. Linked List"],
        "answer": "C",
        "solution": "A stack follows LIFO: Last In, First Out."
    },

    {
        "question": "What is the time complexity of binary search on a sorted array?",
        "options": ["A. O(n)", "B. O(n²)", "C. O(log n)", "D. O(1)"],
        "answer": "C",
        "solution": "Binary search eliminates half of the remaining elements at every step, giving O(log n) complexity."
    },

    {
        "question": "Which scientist proposed the three laws of motion?",
        "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B",
        "solution": "Isaac Newton formulated the three laws of motion."
    },

    {
        "question": "What is the primary function of a transformer in an electrical power system?",
        "options": [
            "A. Convert AC to DC",
            "B. Store electrical energy",
            "C. Increase or decrease AC voltage",
            "D. Generate electricity"
        ],
        "answer": "C",
        "solution": "A transformer changes the voltage level of AC power while maintaining the same frequency."
    }
]

prices = [
    100,
    200,
    300,
    500,
    1000,
    2000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1000000
]
i = 0
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer =input("Enter the option you want to select:").upper()

    if user_answer == q["answer"]:
        print("you've choosed the correct option")
        
        print("congo u have won -", prices[i])
        i += 1

    else:
        print("you've guessed wrong ans , the correct option would be :", q["answer"])
        print(q["solution"])
        print("Wrong!")
        break
    
   


