
#!/bin/bash

echo "=== INFORMAÇÕES DO SERVIDOR ==="
echo "CPU Load: $(uptime | awk -F 'load average:' '{ print $2 }')"
echo "Memória Livre: $(free -h | awk '/Mem/{print $7}')"
echo "Espaço em Disco: $(df -h / | awk 'NR==2 {print $4}')"
