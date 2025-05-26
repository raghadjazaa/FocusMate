import random

def generate_sample_questions():
    all_questions = [
        {
            'question': "Which layout manager divides the frame into five regions like North, South, East, West, and Center?",
            'options': ["GridLayout", "BorderLayout", "FlowLayout", "NullLayout"],
            'answer': "BorderLayout"
        },
        {
            'question': "Which layout allows manual control over component positions and sizes?",
            'options': ["GridLayout", "BorderLayout", "FlowLayout", "NullLayout"],
            'answer': "NullLayout"
        },
        {
            'question': "Which of the following is NOT a Swing component?",
            'options': ["JButton", "JFrame", "Frame", "JRadioButton"],
            'answer': "Frame"
        },
        {
            'question': "Which method sets the window to close when the user clicks the close button?",
            'options': ["setVisible()", "setBounds()", "setDefaultCloseOperation()", "setCloseFrame()"],
            'answer': "setDefaultCloseOperation()"
        },
        {
            'question': "In GridLayout, how are the components arranged?",
            'options': ["Based on preferred size", "In fixed size regions", "In order of addition", "Randomly"],
            'answer': "In order of addition"
        },
        {
            'question': "AWT stands for:",
            'options': ["Advanced Widget Toolkit", "Abstract Window Toolkit", "Application Window Toolkit", "Absolute Window Toolkit"],
            'answer': "Abstract Window Toolkit"
        },
        {
            'question': "Swing components are part of which package?",
            'options': ["java.awt", "javax.swing", "java.ui", "swing.java"],
            'answer': "javax.swing"
        },
        {
            'question': "Which method sets the layout manager for a container?",
            'options': ["setManager()", "setLayout()", "setFrame()", "setComponentLayout()"],
            'answer': "setLayout()"
        },
        {
            'question': "What is the parent class of all AWT components?",
            'options': ["Component", "Container", "JComponent", "Window"],
            'answer': "Component"
        },
        {
            'question': "Which method makes a frame visible?",
            'options': ["setVisible(true)", "show()", "display()", "makeVisible()"],
            'answer': "setVisible(true)"
        },
        {
            'question': "Which layout places components in a single row, wrapping as needed?",
            'options': ["FlowLayout", "GridLayout", "BorderLayout", "RowLayout"],
            'answer': "FlowLayout"
        },
        {
            'question': "What class is used to create a button in Swing?",
            'options': ["Button", "JButton", "SwingButton", "AWTButton"],
            'answer': "JButton"
        },
        {
            'question': "Which class is used to group radio buttons in Swing?",
            'options': ["JRadioGroup", "ButtonGroup", "RadioGroup", "JRadioBox"],
            'answer': "ButtonGroup"
        },
        {
            'question': "Which layout gives all components equal size in rows and columns?",
            'options': ["FlowLayout", "GridLayout", "BorderLayout", "FlexLayout"],
            'answer': "GridLayout"
        },
        {
            'question': "Which component is used to get user text input?",
            'options': ["JLabel", "JTextField", "JPanel", "JPasswordField"],
            'answer': "JTextField"
        }
    ]

    return random.sample(all_questions, 7)