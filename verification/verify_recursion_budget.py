"""Exact checks for the enlarged root-prime cap. Analytic transfer is not tested."""
from fractions import Fraction as F
import json

t = F(9, 16)
tau = F(19, 16)
g = F(43, 8)
cap = 18 + 1/tau
C = F(457, 5)
theta = tau/4

def m1(r):
    return (sum((t**i for i in range(r)), F(0)) + r*t**r)/2

def m2(r):
    return m1(r) + t**r

assert m1(4) == F(40261, 32768)
assert m2(2) == F(181, 128)
for r in range(30):
    assert m1(r+1)-m1(r) == t**r * F(25-7*r, 32)
    assert m2(r+1)-m2(r) == t**r * F(11-7*r, 32)
    assert (sum((t**i for i in range(r)), F(0))+2*t**r)/2 == F(8, 7)-t**r/7
    assert m1(r) <= m1(4)
    assert m2(r) <= m2(2)

ap_gap = F(27,16) - tau*m2(2)
failed_root_ap_gap = (3-tau/2)/8-tau/2
root_ap_gap = (g-tau/2)/8-tau/2
rat_scale = (g-tau/2)/18
rat_gap = rat_scale - F(2,15)
rat_density = F(2,3)*rat_scale
rat_mean_gap = 4-rat_density-F(382,100)
rat_boundary_gap = F(19,100)-rat_density-F(1,100)
fibre_gap = 8-g-tau-F(8,7)*tau
sampler_gap = 7-g
derivative_shift_gap = 8-g
rough_prefix_gap = F(147,100) - tau*m1(4)
rough_rank_gap = F(83,1000) - F(147,100)/F(891,50)
root_induction_slack = 2*(C-cap)**3 - C**3
descent_induction_slack = 64*(C-cap-F(41,20))**3-19*C**3
assert ap_gap == F(17,2048) and ap_gap > 0
assert failed_root_ap_gap == -F(75,256) and failed_root_ap_gap < 0
assert root_ap_gap == F(1,256) and root_ap_gap > 0
assert rat_scale == F(17,64)
assert rat_gap == F(127,960) and rat_gap > 0
assert rat_density == F(17,96)
assert rat_mean_gap == F(7,2400) and rat_mean_gap > 0
assert rat_boundary_gap == F(7,2400) and rat_boundary_gap > 0
assert fibre_gap == F(9,112) and fibre_gap > 0
assert sampler_gap == F(13,8) and sampler_gap > F(98,100)
assert derivative_shift_gap == F(21,8) and derivative_shift_gap > 0
assert rough_prefix_gap > 0 and rough_rank_gap > 0
assert root_induction_slack > 0
assert descent_induction_slack > 0
assert F(17,100) < F(18,100) < F(19,100) < F(1,5)
assert C > 38

out = {
    'tau': str(tau), 'g': str(g), 'root_trial_coefficient': str(cap),
    'candidate_time_coefficient': str(C), 'descendant_power': str(theta),
    'ap_conductor_gap': str(ap_gap), 'rational_admissibility_gap': str(rat_gap),
    'failed_g3_root_conductor_gap': str(failed_root_ap_gap),
    'repaired_root_conductor_gap': str(root_ap_gap),
    'root_rational_density_coefficient': str(rat_density),
    'root_mean_margin_over_3p82': str(rat_mean_gap),
    'root_boundary_margin_beyond_0p01': str(rat_boundary_gap),
    'fibre_width_gap': str(fibre_gap), 'global_sampler_width_gap': str(sampler_gap),
    'leading_derivative_shift_width': str(derivative_shift_gap),
    'rough_prefix_gap': str(rough_prefix_gap), 'rough_rank_gap': str(rough_rank_gap),
    'root_induction_cubic_slack': str(root_induction_slack),
    'descent_induction_cubic_slack': str(descent_induction_slack),
    'scope': 'Exact rational budget and path identities only; no analytic estimate is certified.'
}
print(json.dumps(out, indent=2))
