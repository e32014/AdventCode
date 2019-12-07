import math


def dirs_to_segments(wire):
    posx = 0
    posy = 0
    segments = []
    for dir in wire:
        segment = [(posx, posy)]
        direction = dir[0]
        length = int(dir[1:])
        if direction == "L":
            posx -= length
        elif direction == "R":
            posx += length
        elif direction == "U":
            posy += length
        elif direction == "D":
            posy -= length
        segment.append((posx, posy))
        segments.append(segment)
    return segments


def testIntersection(seg1, seg2):
    seg1Hori = seg1[0][1] == seg1[1][1]
    seg2Hori = seg2[0][1] == seg2[1][1]
    if seg1Hori == seg2Hori:
        return None
    if seg1Hori:
        if min(seg2[0][1], seg2[1][1]) <= seg1[0][1] <= max(seg2[0][1], seg2[1][1]) and \
                min(seg1[0][0], seg1[1][0]) <= seg2[0][0] <= max(seg1[0][0], seg1[1][0]):
            return seg2[0][0], seg1[0][1]
    if seg2Hori:
        if min(seg1[0][1], seg1[1][1]) <= seg2[0][1] <= max(seg1[0][1], seg1[1][1]) and \
                min(seg2[0][0], seg2[1][0]) <= seg1[0][0] <= max(seg2[0][0], seg2[1][0]):
            return seg1[0][0], seg2[0][1]

    return None


def dist_seg(segment):
    return math.sqrt((segment[0][0] - segment[1][0]) ** 2 + (segment[0][1] - segment[1][1]) ** 2)


def cost_on_wire(wire, intersect):
    total = 0
    for i in range(0, len(wire) -1):
        total += dist_seg(wire[i])
    lastSeg = [wire[-1][0], intersect]
    total += dist_seg(lastSeg)
    return total


file = open("input.txt")
wire1 = file.readline().split(",")
wire2 = file.readline().split(",")

wire1Segs = dirs_to_segments(wire1)
wire2Segs = dirs_to_segments(wire2)

minCost = -1
closest = None
for i in range(0, len(wire1Segs)):
    for j in range(0, len(wire2Segs)):
        sect = testIntersection(wire1Segs[i], wire2Segs[j])
        if sect is not None and sect != (0, 0):
            cost = cost_on_wire(wire1Segs[0:i+1], sect) + cost_on_wire(wire2Segs[0:j+1], sect)
            if minCost == -1 or cost < minCost:
                minCost = cost
                closest = sect

print(closest)
print(minCost)
