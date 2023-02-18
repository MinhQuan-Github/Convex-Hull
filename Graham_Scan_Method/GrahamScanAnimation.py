import sys
import numpy as np
import matplotlib.pyplot as plt


class GrahamScan:
    # Function to know if we have a CCW turn
    @staticmethod
    def RightTurn(p1, p2, p3):
        if (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0]):
            return False
        return True

    # Main algorithm:
    def GrahamScan(self, P):
        # Sort the set of points
        P.sort()

        # Convert the list to numpy array
        P = np.array(P)

        # Create a new fig
        plt.figure()

        # Initialize the upper part
        L_upper = [P[0], P[1]]

        # Compute the upper part of the hull
        for i in range(2, len(P)):
            L_upper.append(P[i])
            while len(L_upper) > 2 and not self.RightTurn(L_upper[-1], L_upper[-2], L_upper[-3]):
                del L_upper[-2]
            L = np.array(L_upper)

            # Clear plt.fig
            plt.clf()
            # Plot lines
            plt.plot(L[:, 0], L[:, 1], 'b-', picker=5)
            # Plot points
            plt.plot(P[:, 0], P[:, 1], ".r")
            # No axis
            plt.axis('off')
            # Close plot
            plt.show(block=False)
            # Mini-pause before closing plot
            plt.pause(0.0000001)

        # Initialize the lower part
        L_lower = [P[-1], P[-2]]

        # Compute the lower part of the hull
        for i in range(len(P) - 3, -1, -1):
            L_lower.append(P[i])
            while len(L_lower) > 2 and not self.RightTurn(L_lower[-1], L_lower[-2], L_lower[-3]):
                del L_lower[-2]
            L = np.array(L_upper + L_lower)

            # Clear plt.fig
            plt.clf()
            # Plot lines
            plt.plot(L[:, 0], L[:, 1], 'b-', picker=5)
            # Plot points
            plt.plot(P[:, 0], P[:, 1], ".r")
            # No axis
            plt.axis('off')
            # Close plot
            plt.show(block=False)
            # Mini-pause before closing plot
            plt.pause(0.0000001)

        del L_lower[0]
        del L_lower[-1]
        # Build the full hull
        L = L_upper + L_lower
        plt.axis('off')
        plt.show()
        return np.array(L)

    def run(self):
        try:
            N = int(sys.argv[1])
        except:
            N = int(input("Introduce N: "))

        # By default we build a random set of N points with coordinates in [-300,300)x[-300,300):
        P = [(np.random.randint(-300, 300), np.random.randint(-300, 300)) for _ in range(N)]
        L = self.GrahamScan(P)


if __name__ == '__main__':
    objc = GrahamScan()
    objc.run()
