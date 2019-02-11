#include"graphics.h" 
#define ROUND(a) ((int)(a+0.5)) 
int clipTest (float p,float q, float * tl, float * t2) 
{ 
float r ; 
int retVal = TRUE; 
  
//line entry point 
if (p < 0.0) {     
      
    r = q /p ; 
      
    // line portion is outside the clipping edge 
    if ( r > *t2 )                          
    retVal = FALSE; 
      
    else
    if (r > *t1 ) 
    *tl = r;  
} 
  
else
  
//line leaving point 
if (p>0.0) {                              
    r = q/p ; 
      
    // line portion is outside      
    if ( r<*t1 )                          
        retVal = FALSE;     
          
    else i f (r<*t2) 
        *t2 = r; 
} 
  
// p = 0, so line is parallel to this clipping edge  
else    
  
// Line is outside clipping edge  
if (q<0.0)                                  
retVal = FALSE; 
  
return ( retVal ) ; 
} 
  
void clipLine (dcPt winMin, dcPt winMax, wcPt2 pl , wcPt2 p2)  
  
{  
float t1 = 0.0, t2 = 1.0, dx = p2.x-p1.x, dy; 
  
 // inside test wrt left edge 
if(clipTest (-dx, p1.x - winMin.x, &t1, &t2))     
  
 // inside test wrt right edge  
if(clipTest (dx, winMax.x - p1.x, &t1, &t2))  
  
{                 
    dy = p2.y - p1.y; 
      
    // inside test wrt bottom edge  
    if(clipTest (-dy, p1.y - winMin.y, &t1, &t2)) 
      
        // inside test wrt top edge  
        if(clipTest (dy, winMax.y - p1.y, &t1, &t2)) { 
              
        if(t2 < 1.0) { 
            p2.x = p1.x + t2*dx; 
            p2.y = p1.y + t2*dy; 
        } 
          
        if(t1 > 0.0) { 
            p1.x += t1*dx; 
            p1.y += t1*dy; 
        } 
          
        lineDDA ( ROUND(p1.x), ROUND(p1.y), ROUND(p2.x), ROUND(p2.y) ); 
          
        } 
} 
  
}  

