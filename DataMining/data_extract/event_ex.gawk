#!/usr/bin/awk -f

BEGIN       {
            recno = 1;
            event= "-";
            }
/Event-/{
            if(recno > 1)
                {
                print event;
                }
            recno++;
            event = "";
            for(fn = 2; fn <= NF; fn++) event = event " " $fn;
            }
