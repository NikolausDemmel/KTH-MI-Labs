function [ mu sigma p alpha, classes ] = adaboost( data, T )
    w = ones(size(data, 1), 1) / size(data, 1);
    mu = zeros(T, 2, 2);
    sigma = zeros(T, 2, 2);
    p = zeros(T, 2);
    alpha = zeros(T, 1);
    classes = [0; 1];
    for t=1:T
        [mu(t,:,:) sigma(t,:,:)] = bayes_weight(data, w);
        p(t,:) = prior(data, w);
        g = discriminant(data(:,1:2), reshape(mu(t,:,:),2,2), reshape(sigma(t,:,:),2,2), reshape(p(t,:,:),2,1));
        [dummy class] = max(g, [], 2);
        class = ((class - 1) == (data(:,end)));
        e = 1.0 - sum(class .* w);
        alpha(t) = 1/(2 * log((1 - e) / e));
        w = w .* ((class * exp(-alpha(t))) + ((1 - class) * exp(alpha(t))));
        w = w / sum(w);
    end    

end

