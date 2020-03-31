Google Search Bot with Selenium to the given domains with search keywords


echo "export PATH=\"\$PATH:$HOME/bin\"" >> ~/.bashrc
echo "export PATH=\"$HOME/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc

**note for if short version
cube_numbers = [n**3 for n in range(1,10) if n%2 == 1]
|==
cube_numbers = []
  for n in range(0,10):
    if n % 2 == 1:
      cube_numbers.append(n**3)