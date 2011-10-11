function c = adaboost_discriminant( data, mu, sigma, p, alpha, classes, T)
    M = size(data,1);
    c = zeros(M,1);
    max_val = ones(M, 1) * -inf;
    for i=1:2
        current = zeros(M, 1);
        for t=1:T
            g = discriminant(data(:, 1:2), mu(:,:,t), sigma(:, :,t), p(t, :));
            [dummy class] = max(g, [], 2);
            delta = (classes(class) == classes(i));
            current = current + (alpha(t) * delta);
        end
        for m = 1:M
            if current(m) > max_val(m)
                max_val(m) = current(m);
                c(m) = classes(i);
            end
        end
    end
end

