import math

def calculate(a,b,c):
    try:
        a=float(a)
        b=float(b)
        c=float(c)
    #Two real roots: call the tworealroots function
        if b**2-4*a*c>0:
          answer=tworealroots(a,b,c)
    #Two complex roots: call the imajroots function
        elif b**2-4*a*c<0:
            answer=imajroots(a,b,c)
    #One real root: call the onerealroot function
        elif b**2-4*a*c==0:
          answer=oneroot(a,b,c)
    #For some reason I wasn't getting a divisionByZero error when I tested with a=0.  I raised a valueError in such a case.
        if a==0:
          raise ValueError
    except:
        answer = "Got an error.  Make sure that you enter only numbers and that the value of a is not equal to zero."

    return answer

def imajroots(a,b,c):
  alpha=-b/(2*a)
  beta=math.sqrt(abs(b**2-4*a*c))/(2*a)

  if alpha==0:
    x1=str(round(beta,2))+"i"
    x2=str(round(beta*-1,2))+"i"
  else:
    x1=str(round(alpha,2))+"+"+str(round(beta,2))+"i"
    x2=str(round(alpha,2))+"-"+str(round(beta,2))+"i"
  answer= f"Your function produces two complex roots, x={x1} and x={x2}."
  return answer


def tworealroots(a,b,c):
  x1=round((-b+(b**2-4*a*c)**0.5)/(2*a),2)
  x2=round((-b-(b**2-4*a*c)**0.5)/(2*a),2)
  answer=f"Your function produces two real roots, x={x1} and x={x2}."
  return answer

def oneroot(a,b,c):
  x1=round((-b+(b**2-4*a*c)**0.5)/(2*a),2)
  answer=f"Your function produces one real root, x={x1} with multiplicity of 2."
  return answer