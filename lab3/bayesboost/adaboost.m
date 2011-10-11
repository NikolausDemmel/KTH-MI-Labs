function [ mu sigma p alpha, classes ] = adaboost( data, T )
    [M N] = size(data);
    w = ones(M, 1) / M;
    mu = zeros(2, 2, T);
    sigma = zeros(2, 2, T);
    p = zeros(T,2);
    alpha = zeros(T,1);
    classes = [0; 1];
    for t=1:T
        [mu(:,:,t) sigma(:,:,t)] = bayes_weight(data, w);
        p(t,:) = prior(data, w);
        g = discriminant(data(:,1:2), mu(:,:,t), sigma(:,:,t), p(t,:));
        [dummy class] = max(g, [], 2);
        delta = ((class - 1) == (data(:,end)));
        e = 1.0 - sum(delta .* w);
        alpha(t) = 0.5 * log((1 - e) / e);
        w1 = delta * exp(-alpha(t));
        w2 = (1 - delta) * exp(alpha(t));
        w = w .* (w1 + w2);
        w = w / sum(w);
    end    

end

