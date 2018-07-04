"""
Calculates the modifier from a stat like str or dex
"""
def statMod(value):
  m = (value - 10) / 2
  # this accounts for negative bonus rounding
  if m < 0:
    m = m - 0.5
  return int(m)