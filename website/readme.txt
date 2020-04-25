Website: can access website in Binghamton when connected to Binghamton WiFI. At wcp23.pods.bu.int.

To edit website: Must be in a lab room connected to ethernet. To edit the website you would have to ssh into the website ex- podsid@wcp23.pods.bu.int The index file is at var/www/html.

Website folder documents from github:
Index.html and pattern.js:
  -main html code for website.
  -For now you can only draw on canvas (white box) while holding your mouse left button. Once you lift your mouse up you can’t draw anymore
  -to get rid of this just comment out the var first from code (used in function findxy and erase function)
  -Original code to draw on canvas: https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse
  -Once you press the erase button you clear the canvas and can start drawing again
    -Didn’t manage to get the save to work properly.
  -Save should save the image on the server into the database. Should be in a jpeg or png format.
  -Image should be able to be converted to svg in order for it to be read properly. 
      -Need to download libraries: potrace and imagemagick-6.q16
      -Tried to download them on the server but it didn’t work
      -Use these UNIX commands to convert:
                convert <name>.png -resize 750x750 <name>.png
                convert <name>.png <name>.pnm
                potrace <name>.pnm -s -o <name>.svg
      -I have a tcl script that can convert 8 pictures automatically. Just type in tclsh and paste code in. (in stefano branch under website -> pattern conversion)



