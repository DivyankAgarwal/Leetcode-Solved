class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True

            if tx > ty:
                # If ty matches sy, we just need to check if we can reduce tx to sx
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx %= ty #tx = tx - ty
            else:
                # If tx matches sx, we just need to check if we can reduce ty to sy
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty %= tx #ty = ty-sy

        return False