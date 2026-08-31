```bash
#!/bin/bash
echo "Updating system and installing network discovery tools for Yaqith..."
sudo apt-get update
sudo apt-get install nmap arp-scan -y
echo "Installation complete!"
