function c = adaboost_discriminant( data, mu, sigma, p, alpha, classes, T)
    M = size(data,1);
    c = zeros(M,1);
    max_val = ones(M, 1) * -inf;
    for i=1:size(classes,1)
        current = zeros(M, 1);
        for t=1:T
            g = discriminant(data(:, 1:2), reshape(mu(t,:,:),2,2), reshape(sigma(t, :, :),2,2) , reshape(p(t, :),2,1));
            [dummy class] = max(g, [], 2);
            delta = (classes(class) == classes(i));
            current = current + (alpha(t) * delta);
        end
        for m = 1:M
            if current(m) > max_val(m)
                max_val(m) = current(m);
                c(m) = i;
            end
        end
    end
end

