#!/usr/bin/bash
ssh -p 22022 -i /etc/ssh/id_rsa -L 5900:192.168.11.84:5900 qdl@aditum.helmholtz-berlin.de


