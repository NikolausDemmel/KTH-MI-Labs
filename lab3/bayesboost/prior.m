function [p] = prior(data,w)
%this function computes the prior class probabilities
%data = data set with last column containing the classes
%w = weight vector for weighting training instances (optional)
[m,n] = size(data);
if (nargin==1)
  w=ones(m,1);
end
classes = unique(data(:,n));
for i=1:length(classes)
  index=find(data(:,n)==classes(i));
  p(i)=sum(w(index));
end
p=p/sum(w);