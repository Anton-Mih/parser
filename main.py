from tkinter import messagebox
from file_manager import add_new_word
def main():
  while True:
    user_choise = input('enter number:\n')
    try:
      user_choise = int(user_choise)
    except Exception:
      messagebox.showerror("Error", "Enter a number not word")
      continue
    else:
      if user_choise == 0:
        break
      elif user_choise == 1:
        add_new_word()
      elif user_choise == 2:
        pass
      elif user_choise == 3:
        pass
      elif user_choise == 4:
        pass
      elif user_choise == 5:
        pass
      elif user_choise == 6:
        pass
      elif user_choise == 7:
        pass
      else:
        print('you done wrong choise')
    
main()
