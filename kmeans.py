import numpy as np

def kmeans(observation_array, initial_means):
    k = len(initial_means)
    round = 0
    while True:
        # Assign each observation to the nearest mean
        clusters = [[] for _ in range(k)]
        for obs in observation_array:
            nearest_mean_idx = np.argmin([np.abs(obs - mean) for mean in initial_means])
            clusters[nearest_mean_idx].append(obs)
        
        # Update the means
        new_means = [np.mean(cluster) if cluster else mean for cluster, mean in zip(clusters, initial_means)]
        
        # Check for convergence
        if np.allclose(new_means, initial_means):
            break
        
        initial_means = new_means
        round += 1

        print(f"Round {round}:")
        print(f"-means: {initial_means}")
        for i, cluster in enumerate(clusters):
            print(f'    Cluster {i + 1}:', cluster)
    
    return clusters, initial_means

# Example usage:
if __name__ == "__main__":
    observations = np.array([0.1,0.3,0.5,1.0,2.2,3.0,4.1,4.4,4.7])
    initial_means = np.array([0.2,0.3,3.1,4.55])

    clusters, final_means = kmeans(observations, initial_means)

    for i, cluster in enumerate(clusters):
        print(f'Cluster {i + 1}:', cluster)

    print('Final Means:', final_means)