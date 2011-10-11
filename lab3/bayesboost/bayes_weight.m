function [ mu sigma ] = bayesweight( data, w)

    mu = zeros(2,2);
    sigma = zeros(2,2);
    c = [0.0 1.0];
    
    for i = 1:2
        M = 0;
        for j = 1:size(data,1)
            if data(j,3) == c(i)
                M = M + w(j);
            end
        end
        for n = 1:2
            for j = 1:size(data,1)
                if data(j,3) == c(i)
                    mu(i,n) = mu(i,n) + data(j,n) .* w(j);
                end
            end
            %if M ~= 0
                mu(i,n) = mu(i,n) ./ M;
            %end
            for j = 1:size(data,1)
                if data(j,3) == c(i)
                    sigma(i,n) = sigma(i,n) + w(j) .* (data(j,n) - mu(i,n)).^2;
                end
            end
            %if M ~= 0
                sigma(i,n) = sigma(i,n) ./ M;
            %end
            sigma(i,n) = sqrt(sigma(i,n));
        end
    end

end

