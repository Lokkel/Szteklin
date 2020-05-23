#
# This script requir
#
# run on raspberry pi
scp pi@192.168.2.199:/home/pi/picam/*.jpg ./
ssh pi@192.168.2.199 << EOF
   mv ./picam/*.jpg ./picam/archive
EOF

