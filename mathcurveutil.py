import bpy
import math
from math import cos, sin, pi
from mathutils import Vector

tau = 2 * pi
w = 1

#set custom int value
num_points = 15
amp = lambda i: 5 if (i % 2) else 7
pos = lambda f, i: f(i/num_points*tau) * amp(i)
listOfVectors = [(pos(sin, i), pos(cos, i), 0) for i in range(num_points)] 

def MakePolyLine(objname, curvename, cList):
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')
    curvedata.dimensions = '3D'
    
    objectdata = bpy.data.objects.new(objname, curvedata)
    objectdata.location = (0, 0, 0)
    bpy.context.scene.objects.link(objectdata)
    
       
    polyline = curvedata.splines.new('NURBS')
    polyline.points.add(len(cList)-1)
    for num in range(len(cList)): 
        polyline.points[num].co = (cList[num])+(w,)
                
          
    polyline.order_u = len(polyline.points)-1
    polyline.use_endpoint_u = True
    polyline.use_cyclic_u = True
    
MakePolyLine("VesselCurveObject", "VesselCurve", listOfVectors)

    
