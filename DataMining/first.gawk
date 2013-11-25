#!/usr/bin/awk -f

BEGIN       {
            recno = 1;
            title= "-"; subtitle = "-"; author= "-"; edition= "-";
            place= "-"; publisher= "-"; pubdate= "-"; pages= "-";
            isbn= "-"; callno= "-"; accno = "-";
            }
/Title/     {
            if(recno > 1)
                {
                print title, "\t", subtitle, "\t", author, "\t", edition, "\t",
                    place, "\t", publisher, "\t", pubdate, "\t", pages, "\t",
                    isbn, "\t", callno, "\t", accno;
                }
            recno++;
            subtitle = "-"; author= "-"; edition= "-";
            place= "-"; publisher= "-"; pubdate= "-"; pages= "-";
            isbn= "-"; callno= "-"; accno = "-";
            title = "";
            for(fn = 3; fn <= NF; fn++) title = title " " $fn;
            }
/Subtitle/  { subtitle = ""; for(fn = 3; fn <= NF; fn++) subtitle = subtitle " " $fn; }
/Class No/  { callno = ""; for(fn = 4; fn <= NF; fn++) callno = callno " " $fn; }
/Accn Nos/  { accno = ""; for(fn = 4; fn <= NF; fn++) accno = accno " " $fn; }
/Publ.Plc/  { place = ""; for(fn = 3; fn <= NF; fn++) place = place " " $fn; }
/Publ.  / { publisher = ""; for(fn = 3; fn <= NF; fn++) publisher = publisher " " $fn; }
/Publ Dt/ { pubdate = ""; pubdate = $4;} 
/Pages/ { pages = ""; pages = $3;}
/ISBN/ { isbn = ""; isbn = $3;}
/Author/ { author = ""; for( fn = 3; fn <= NF; fn++) author = author " " $fn;}
/Edition/ { edition = ""; edition = $3;}
